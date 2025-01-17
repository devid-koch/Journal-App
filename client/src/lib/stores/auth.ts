import { writable } from 'svelte/store';

export interface AuthState {
  isAuthenticated: boolean;
  user: User | null;
  token: string | null;
}

export interface User {
  id: number;
  email: string;
  name: string;
}

let storedToken = null;

if (typeof window !== 'undefined') {
  storedToken = localStorage.getItem('accessToken');
}

const initialState: AuthState = storedToken
  ? {
      isAuthenticated: true,
      user: null,
      token: storedToken,
    }
  : {
      isAuthenticated: false,
      user: null,
      token: null,
    };

export const authStore = writable<AuthState>(initialState);

// Action to update the store when logging in
export const login = (user: User, token: string) => {
  authStore.set({
    isAuthenticated: true,
    user,
    token,
  });
};