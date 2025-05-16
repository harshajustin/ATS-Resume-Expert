import { useState } from 'react';
import { Card, CardContent, Typography, Button } from '@mui/material';
import useStore from '../store/store';

function ResumePreview() {
  const { resumes, selectedResume, setSelectedResume } = useStore();
  const [showFullScreen, setShowFullScreen] = useState(false);

  if (!Object.keys(resumes).length) {
    return null;
  }

  const handleResumeSelect = (fileName: string) => {
    setSelectedResume(fileName);
  };

  return (
    <div className="mt-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <Typography variant="h6" gutterBottom>
            Available Resumes
          </Typography>
          {Object.keys(resumes).map((fileName) => (
            <Button
              key={fileName}
              variant={selectedResume === fileName ? "contained" : "outlined"}
              onClick={() => handleResumeSelect(fileName)}
              fullWidth
              className="mb-2"
            >
              {fileName}
            </Button>
          ))}
        </div>

        {selectedResume && (
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Results for {selectedResume}
              </Typography>
              {Object.entries(resumes[selectedResume].responses).map(([action, response]) => (
                <div key={action} className="mb-4">
                  <Typography variant="subtitle1" color="primary">
                    {action}
                  </Typography>
                  <Typography variant="body1">
                    {response}
                  </Typography>
                </div>
              ))}
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}

export default ResumePreview;