import axios from './axios'; // Import the global axios instance

export const getJournalEntries = async () => {
  const response = await axios.get('/journal/entries/');
  return response.data;
};

export const createJournalEntry = async (content: string) => {
  const response = await axios.post('/journal/entries/', { content });
  return response.data;
};


export const analyzeJournalEntry = async (content: string) => {
  const response = await axios.post('/journal/analyze-entry/', { content });
  return response.data;
};

export const deleteJournalEntry = async (id: number) => {
  const response = await axios.delete(`/journal/journal-entries/${id}/`)
  return response.data;
}


export const updateJournalEntry = async (id:number,content: string) => {
  const response = await axios.put(`/journal/journal-entries/${id}/`, { content })
  return response.data;
}

export const generatePromptText = async (content: string) => {
  const response = await axios.post('/journal/generate-prompt/', { content })
  return response.data;
}