import { useState } from 'react';
import { TextField, Button, Radio, RadioGroup, FormControlLabel, FormControl, FormLabel } from '@mui/material';
import { useDropzone } from 'react-dropzone';
import useStore from '../store/store';
import ResumePreview from '../components/ResumePreview';
import ActionSelector from '../components/ActionSelector';

function Home() {
  const [jobDescription, setJobDescription] = useState('');
  const { userMode, setUserMode, addResumes } = useStore();

  const { getRootProps, getInputProps } = useDropzone({
    accept: {
      'application/pdf': ['.pdf'],
    },
    maxFiles: 10,
    onDrop: (acceptedFiles) => {
      addResumes(acceptedFiles);
    },
  });

  return (
    <div className="space-y-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">
          Optimize your resume for Applicant Tracking Systems (ATS)
        </h1>

        <FormControl component="fieldset" className="mb-6">
          <FormLabel component="legend">Choose user:</FormLabel>
          <RadioGroup
            row
            value={userMode}
            onChange={(e) => setUserMode(e.target.value as 'Recruiter' | 'Student')}
          >
            <FormControlLabel value="Recruiter" control={<Radio />} label="Recruiter" />
            <FormControlLabel value="Student" control={<Radio />} label="Student" />
          </RadioGroup>
        </FormControl>

        <TextField
          fullWidth
          multiline
          rows={4}
          label="Job Description"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          className="mb-6"
        />

        <div {...getRootProps()} className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center cursor-pointer hover:border-blue-500 transition-colors">
          <input {...getInputProps()} />
          <p>Drag and drop PDF resumes here, or click to select files</p>
          <p className="text-sm text-gray-500">(Maximum 10 files)</p>
        </div>

        <ActionSelector />
        <ResumePreview />
      </div>
    </div>
  );
}

export default Home;