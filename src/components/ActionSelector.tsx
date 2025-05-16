import { useState } from 'react';
import { Button, FormControl, FormLabel, RadioGroup, FormControlLabel, Radio } from '@mui/material';
import useStore from '../store/store';
import { getPrompts } from '../utils/prompts';

function ActionSelector() {
  const { userMode, resumes, selectedResume, addResponse } = useStore();
  const [selectedAction, setSelectedAction] = useState<string>('');
  const prompts = getPrompts(userMode);

  const handleSubmit = async () => {
    if (!selectedResume || !selectedAction) return;

    try {
      // TODO: Implement API call to process resume
      const response = "Sample response"; // Replace with actual API call
      addResponse(selectedResume, selectedAction, response);
    } catch (error) {
      console.error('Error processing resume:', error);
    }
  };

  return (
    <div className="mt-8">
      <FormControl component="fieldset" className="w-full">
        <FormLabel component="legend">Choose an Action:</FormLabel>
        <RadioGroup
          row
          value={selectedAction}
          onChange={(e) => setSelectedAction(e.target.value)}
        >
          {Object.keys(prompts).map((action) => (
            <FormControlLabel
              key={action}
              value={action}
              control={<Radio />}
              label={action}
            />
          ))}
        </RadioGroup>
      </FormControl>

      <Button
        variant="contained"
        color="primary"
        onClick={handleSubmit}
        disabled={!selectedResume || !selectedAction}
        className="mt-4"
      >
        Submit
      </Button>
    </div>
  );
}

export default ActionSelector;