import { create } from 'zustand';

interface Resume {
  file: File;
  preview?: string;
  responses: Record<string, string>;
}

interface Store {
  userMode: 'Recruiter' | 'Student';
  resumes: Record<string, Resume>;
  selectedResume: string | null;
  setUserMode: (mode: 'Recruiter' | 'Student') => void;
  addResumes: (files: File[]) => void;
  setSelectedResume: (fileName: string | null) => void;
  addResponse: (fileName: string, action: string, response: string) => void;
}

const useStore = create<Store>((set) => ({
  userMode: 'Recruiter',
  resumes: {},
  selectedResume: null,
  setUserMode: (mode) => set({ userMode: mode }),
  addResumes: (files) => set((state) => ({
    resumes: {
      ...state.resumes,
      ...Object.fromEntries(
        files.map((file) => [file.name, { file, responses: {} }])
      ),
    },
  })),
  setSelectedResume: (fileName) => set({ selectedResume: fileName }),
  addResponse: (fileName, action, response) => set((state) => ({
    resumes: {
      ...state.resumes,
      [fileName]: {
        ...state.resumes[fileName],
        responses: {
          ...state.resumes[fileName].responses,
          [action]: response,
        },
      },
    },
  })),
}));

export default useStore;