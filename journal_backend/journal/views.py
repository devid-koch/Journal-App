from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from .ai_utils import analyze_entry, generate_prompt


class JournalEntryListCreateView(ListCreateAPIView):
    """
    Handles listing all journal entries for a user and creating new entries.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = JournalEntrySerializer

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        try:
            journal_entry = serializer.save(user=self.request.user)

            # Get AI insights for the newly created journal entry
            insights = analyze_entry(journal_entry.content)

            return Response({
                "entry": JournalEntrySerializer(journal_entry).data,
                "insights": insights
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "error": f"An error occurred while analyzing the entry: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class JournalEntryDetailView(RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single journal entry.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = JournalEntrySerializer

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)
    

    def put(self, request, *args, **kwargs):
        try:
            entry = self.get_object()
            serializer = self.get_serializer(entry, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Journal entry updated successfully",
                "entry": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred while updating the entry: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, *args, **kwargs):
        """
        Custom behavior for deleting a journal entry.
        """
        try:
            entry = self.get_object()
            entry.delete()
            return Response({"message": "Journal entry deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred while deleting the entry: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class JournalEntryAIView(APIView):
    """
    Endpoint to analyze a user's journal entry using AI for insights.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        content = request.data.get("content")
        if not content:
            return Response({"error": "Content is required"}, status=status.HTTP_400_BAD_REQUEST)

        insights = analyze_entry(content)

        return Response({
            "insights": insights
        }, status=status.HTTP_200_OK)


class JournalPromptGenerateView(APIView):
    """
    Endpoint to generate a writing prompt based on the user's previous journal entry.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            content = request.data.get("content", "")

            if not content:
                return Response({
                    "error": "Journal entry content is required."
                }, status=status.HTTP_400_BAD_REQUEST)

            prompt = generate_prompt(content)

            return Response({
                "generatedText": prompt
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "error": f"An error occurred while generating the prompt: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
