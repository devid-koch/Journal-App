<script lang="ts">
    import { createJournalEntry } from '$lib/api/journal';
    import { goto } from '$app/navigation';

    let content = '';
    let message = '';
    let loading=false;

    async function handleCreate() {
        try {
            loading=true;
            await createJournalEntry(content);
            message = 'Journal entry created successfully!';
            goto('/journal');
        } catch (error) {
            loading=false;
            message = 'Failed to create journal entry.';
        }
    }
</script>

<div class="flex justify-center items-center min-h-screen bg-gray-100">
    <form
        on:submit|preventDefault={handleCreate}
        class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-lg"
    >
        <h1 class="text-2xl font-bold mb-4 text-center">New Journal Entry</h1>
        <textarea
            placeholder="Write your entry..."
            bind:value={content}
            required
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-32 resize-none"
        ></textarea>
        <div class="flex items-center gap-2">
        <button
            disabled={loading}
            type="submit"
            class="flex justify-center col-span-1 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-3/4"
        >
            {#if loading}
                <svg
                    class="animate-spin h-5 w-5 mr-3"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                >
                    <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M4 12a8 8 0 118 8"></path>
                </svg>
            {:else}
                Save
            {/if}
        </button>
        <button on:click={()=>goto("/journal")} class="rounded px-4 py-2 border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-blue-100 duration-300">Back</button>
        </div>
        
        {#if message}
            <p class="text-green-500 text-xs italic mt-4 text-center">{message}</p>
        {/if}
    </form>
</div>
