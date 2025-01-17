<script lang="ts">
    import '../app.css';
    import { authStore } from '$lib/stores/auth';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { get } from 'svelte/store';

    onMount(() => {
        const { isAuthenticated } = get(authStore);
        if (!isAuthenticated) {
        goto('/auth/login');
        }
    });
</script>

<slot />
