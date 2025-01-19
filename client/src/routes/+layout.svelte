<script lang="ts">
    import '../app.css';
    import { authStore } from '$lib/stores/auth';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { get } from 'svelte/store';
    import { SvelteToast } from '@zerodevx/svelte-toast'

    onMount(() => {
        const { isAuthenticated } = get(authStore);
        if (!isAuthenticated) {
        goto('/auth/login');
        }
    });
</script>

<SvelteToast/>

<slot />
