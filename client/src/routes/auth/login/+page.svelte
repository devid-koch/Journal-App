<script lang="ts">
    import { loginUser } from '$lib/api/auth';
    import { goto } from '$app/navigation';
    import { toast } from '@zerodevx/svelte-toast';
    import { toastErrorTheme, toastSuccessTheme } from '$lib/toastThemes';
    

    let email = '';
    let password = '';
    let message = '';
    let loading = false;

    async function handleLogin() {
        try {
            loading = true;
            const data = await loginUser(email, password);
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
            toast.push("Login successfull!",toastSuccessTheme)
            goto('/journal');
        } catch (error:any) {
            message = error.response?.data?.detail || 'Login failed.';
            toast.push(message, toastErrorTheme)
            loading = false;
        } finally {
            loading = false;
        }
    }
</script>

<div class="flex justify-center items-center min-h-screen bg-gray-100">
    <form
        on:submit|preventDefault={handleLogin}
        class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-sm"
    >
        <h1 class="text-2xl font-bold mb-4 text-center">Login</h1>
        <div class="mb-4">
            <input
                type="text"
                placeholder="Email"
                bind:value={email}
                required
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
        </div>
        <div class="mb-6">
            <input
                type="password"
                placeholder="Password"
                bind:value={password}
                required
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
        </div>
        <button
            type="submit"
            class={`flex justify-center bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full ${loading && "cursor-not-allowed"}`}
            disabled={loading}
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
                Login
            {/if}
        </button>
        {#if message}
            <p class="text-red-500 text-xs italic mt-4 text-center">{message}</p>
        {/if}

        <div class="mt-4 text-center">
            <p>Don't have an account? 
                <button 
                    class="text-blue-500 hover:underline focus:outline-none" 
                    on:click={() => goto('/auth/register')}
                >
                    Register here
                </button>
            </p>
        </div>
    </form>
</div>
