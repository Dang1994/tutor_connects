import React, { useState } from 'react';

function Feedback() {
  const [feedback, setFeedback] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Feedback submitted: ${feedback}`);
    setFeedback('');
  };

  return (
    <div>
      <h2>Feedback</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          value={feedback}
          onChange={(e) => setFeedback(e.target.value)}
          placeholder="Enter your feedback here"
        ></textarea>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Feedback;
