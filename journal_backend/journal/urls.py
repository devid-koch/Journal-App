from django.urls import path
from .views import JournalEntryListCreateView,JournalEntryDetailView,JournalEntryAIView,JournalPromptGenerateView

urlpatterns = [
    path('entries/', JournalEntryListCreateView.as_view(), name='journal-entries'),
    path('journal-entries/<int:pk>/', JournalEntryDetailView.as_view(), name='journal-detail'),
    path('analyze-entry/', JournalEntryAIView.as_view(), name='analyze-entry'),
    path('generate-prompt/', JournalPromptGenerateView.as_view(), name='generate-prompt')
]
