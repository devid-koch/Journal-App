<script lang="ts">
    import { onMount } from 'svelte';
    import { analyzeJournalEntry, deleteJournalEntry, generatePromptText, getJournalEntries, updateJournalEntry } from '$lib/api/journal';
    import type { JournalEntry } from '../../types/journal';
    import { goto } from '$app/navigation';
    import Loader from '$lib/components/Loader/Loader.svelte';
    import { toast } from '@zerodevx/svelte-toast'
    import { toastErrorTheme, toastSuccessTheme } from '$lib/toastThemes';
    

    let journals: JournalEntry[] = [];
    let error = '';
    let analysisResults: Record<number, { sentiment: string, confidence: number }> = {};

    let editingIndex:any = null;
    let editingContent = '';

    let message = "";
    let analyzeLoading: { [key: number]: boolean } = {};
    let textGenerationloading: { [key: number]: boolean } = {};
    
    function editContent(index:number, content:string) {
        editingIndex = index;
        editingContent = content;
    }

    function cancelEdit() {
        editingIndex = null;
    }

    const deleteEntry = async (id:number)=>{
        try {
            const response = await deleteJournalEntry(id);
            toast.push("Entry deleted!", toastSuccessTheme);
            if(response){
                await getJounals();
            }
        } catch (err) {
            error = "Failed to delete. Please try again later.";
            toast.push(error, toastErrorTheme);
            console.error(err);
        }
    }

    const analyzeAI = async (index: number, content: string) => {
        if(analysisResults[index]){
            return
        }
        try {
            analyzeLoading = { ...analyzeLoading, [index]: true };
            const response = await analyzeJournalEntry(content);
            toast.push("Analyze successfully!", toastSuccessTheme);
            analysisResults[index] = response.insights.insights;
        } catch (err) {
            error = "Failed to analyze. Please try again later.";
            toast.push(error, toastErrorTheme);
            console.error(err);
        } finally{
            analyzeLoading = { ...analyzeLoading, [index]: false };
        }
    };

    const getJounals = async ()=>{
        try {
            const data = await getJournalEntries();
            journals = data;
        } catch (err) {
            error = 'Failed to load journal entries.';
        }
    }


    const saveEdit = async(id:number, updatedContent:string)=>{
        try {
            const response = await updateJournalEntry(id, updatedContent);
            if(response.message){
                message = response.message;
                toast.push(message, toastSuccessTheme);
                cancelEdit();
                await getJounals();
            }
        } catch (err) {
            error = 'Failed to update journal entry.';
            toast.push(error, toastErrorTheme);
        }
    }

    const generateText = async(index:number)=>{
        const prompt = journals[index].content;
        try {
            textGenerationloading = { ...textGenerationloading, [index]: true };
            const response = await generatePromptText(prompt);
            if(response.generatedText){
                toast.push("Text generated successfully!", toastSuccessTheme)
                editingContent = response.generatedText;
            }
        } catch (err) {
            error = 'Failed to generate journal entry text.';
            toast.push(error, toastErrorTheme);
        }
        finally{
            textGenerationloading = { ...textGenerationloading, [index]: false };
        }
        
    }

    const logout = ()=>{
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        goto("/auth/login")
    }

    onMount(async () => {
        await getJounals();
        journals.forEach(journal => {
            analyzeLoading[journal.id] = false;
        });
    });
</script>
<div class="min-h-screen bg-gray-100 p-6">
    <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold mb-4 text-center">AI-Powered Journal</h1>
        <div class="flex gap-5">
            <button class="rounded-lg px-4 py-2 border-2 border-blue-500 text-blue-500 hover:bg-blue-600 hover:text-blue-100 duration-300" on:click={()=> goto("journal/new")}>Add new Journal</button>
            <button on:click={logout}>Log Out</button>
        </div>
    </div>

    {#if journals.length}
        <table class="min-w-full bg-white border-collapse mt-6">
            <thead>
                <tr>
                    <th class="border px-4 py-2 text-left">Sl No</th>
                    <th class="border px-4 py-2 text-left">Content</th>
                    <th class="border px-4 py-2 text-left">Action</th>
                </tr>
            </thead>
            <tbody>
                {#each journals as journal, index}
                    <tr>
                        <td class="border px-4 py-2">{index + 1}</td>
                        <td class="border px-4 py-2 capitalize w-1/2">
                        {#if editingIndex === index}
                            <textarea contenteditable="true" class="editable-content resize-none border-2 border-dashed border-black w-full h-auto" bind:value={editingContent}></textarea>
                        {:else}
                            {journal.content}
                        {/if}</td>
                        <td class="flex items-center gap-2 border px-4 py-2">
                            {#if editingIndex === index}
                            <button 
                                class="rounded-lg px-4 py-2 border-2 border-blue-600 text-blue-600 hover:bg-blue-600 hover:text-white duration-300"
                                on:click={() => saveEdit(journal.id, editingContent)}>
                                Save
                            </button>
                            <button disabled={textGenerationloading[index]} class="w-40 flex justify-center rounded-lg px-4 py-2 border-2 border-yellow-600 text-yellow-600 hover:bg-yellow-600 hover:text-yellow-100 duration-300" on:click={() => generateText(index)}>
                                {#if textGenerationloading[index]}
                                    <Loader/>
                                {:else}
                                    Generate Text
                                {/if}
                            </button>
                            <button
                                class="rounded-lg px-4 py-2 border-2 border-gray-600 text-gray-600 hover:bg-gray-600 hover:text-gray-100 duration-300"
                                on:click={() => cancelEdit()}>
                                Cancel
                            </button>
                        {:else}
                            <button
                            on:click={()=>editContent(index, journal.content)}
                            class="rounded-lg px-4 py-2 border-2 border-gray-600 text-gray-600 hover:bg-gray-600 hover:text-gray-100 duration-300">
                                Edit</button>
                            <button
                                on:click={() => analyzeAI(index, journal.content)}
                                disabled={analyzeLoading[index]}
                                class="w-40 flex justify-center rounded-lg px-4 py-2 border-2 border-green-700 text-green-700 hover:bg-green-700 hover:text-green-100 duration-300"
                            >
                                {#if analyzeLoading[index]}
                                    <Loader/>
                                {:else}
                                Analyze with AI
                                {/if }
                            </button>
                            
                            <button on:click={()=>deleteEntry(journal.id)} class="rounded-lg px-4 py-2 border-2 border-red-600 text-red-600 hover:bg-red-600 hover:text-red-100 duration-300">Delete</button>
                            {/if}
                        </td>
                    </tr>
                    {#if analysisResults[index]}
                        <tr>
                            <td colspan="3" class="border px-4 py-2 text-left">
                                <div>
                                    <p><strong>Sentiment:</strong> {analysisResults[index].sentiment}</p>
                                    <p><strong>Confidence:</strong> {analysisResults[index].confidence}</p>
                                </div>
                            </td>
                        </tr>
                    {/if}
                {/each}
            </tbody>
        </table>
    {:else if error}
        <p class="text-red-500 text-center">{error}</p>
    {:else}
        <p class="text-gray-500 text-center">No entries yet.</p>
    {/if}

   
</div>
