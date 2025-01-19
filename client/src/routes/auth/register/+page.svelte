<script lang="ts">
    import { registerUser } from '$lib/api/auth';
    import { goto } from '$app/navigation';
    import Loader from '$lib/components/Loader/Loader.svelte';
    import { toast } from '@zerodevx/svelte-toast';
    import { toastErrorTheme, toastSuccessTheme } from '$lib/toastThemes';

    let username = '';
    let email = '';
    let password = '';
    let message = '';
    let loading = false;

    async function handleRegister() {
        try {
            loading=true
            await registerUser(username, email, password);
            message = 'Registration successful!';
            toast.push(`${message} Please Login`, toastSuccessTheme)
            goto('/auth/login');
        } catch (error:any) {
            loading=false
            message = error?.response?.data?.email?.[0] || error?.response?.data?.username?.[0] || 'Registration failed.';
            toast.push(message, toastErrorTheme);
        }
    }
</script>

<div class="flex justify-center items-center min-h-screen bg-gray-100">
    <form
        on:submit|preventDefault={handleRegister}
        class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-sm"
    >
        <h1 class="text-2xl font-bold mb-4 text-center">Register</h1>
        <div class="mb-4">
            <input
                type="text"
                placeholder="Username"
                bind:value={username}
                required
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
        </div>
        <div class="mb-4">
            <input
                type="email"
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
            class={`flex justify-center bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full ${loading && "cursor-not-allowed"}`}
            disabled={loading}
        >
            {#if loading}
                <Loader/>
            {:else}
                Register
            {/if}
        </button>
        {#if message}
            <p class="text-red-500 text-xs italic mt-4 text-center">{message}</p>
        {/if}

        <div class="mt-4 text-center">
            <p>Already have an account? 
                <button 
                    class="text-blue-500 hover:underline focus:outline-none" 
                    on:click={() => goto('/auth/login')}
                >
                    Login here
                </button>
            </p>
        </div>
    </form>
</div>
