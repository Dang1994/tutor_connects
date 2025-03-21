import React, { useState } from 'react';
import '../styles/TutorRegistration.css';  // Import the CSS file

const TutorRegistration = () => {
  const [tutorData, setTutorData] = useState({
    // Basic Information
    name: '',
    phone: '',
    email: '',
    address: '',
    location: '',
    
    // Qualifications
    education: '',
    higherEducation: '',
    bachelor: '',
    
    // Specializations
    subjects: [],
    gradeLevels: '',
    
    // Availability
    scheduleFrom: '',
    scheduleUntil: '',
    modeOfTutoring: '',
    
    // Additional Information
    tutoringApproach: '',
    rates: '',
    reviews: '',
    
    // Optional Information
    additionalSkills: '',
    profilePicture: null,
    
    // Consent
    consent: false,
  });

  // Handle input changes
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === 'checkbox') {
      setTutorData({ ...tutorData, [name]: checked });
    } else if (type === 'file') {
      setTutorData({ ...tutorData, [name]: e.target.files[0] });
    } else {
      setTutorData({ ...tutorData, [name]: value });
    }
  };

  const addSubject = (e) => {
    const selectedSubjects = Array.from(e.target.selectedOptions, option => option.value);
    setTutorData({ ...tutorData, subjects: selectedSubjects });
  };

  const toggleBachelor = () => {
    setTutorData((prev) => ({
      ...prev,
      bachelor: prev.bachelor ? '' : ''
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Construct form data for the profile picture (optional file upload)
    const formData = new FormData();
    Object.keys(tutorData).forEach((key) => {
      formData.append(key, tutorData[key]);
    });

    // Post the form data to the Django backend
    const response = await fetch('http://localhost:8000/tutors/register/', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();

    if (response.ok) {
      alert('Tutor registered successfully!');
      setTutorData({
        name: '',
        phone: '',
        email: '',
        address: '',
        location: '',
        education: '',
        higherEducation: '',
        bachelor: '',
        subjects: [],
        gradeLevels: '',
        scheduleFrom: '',
        scheduleUntil: '',
        modeOfTutoring: '',
        tutoringApproach: '',
        rates: '',
        reviews: '',
        additionalSkills: '',
        profilePicture: null,
        consent: false,
      });
    } else {
      alert('Error registering tutor: ' + JSON.stringify(data));
    }
  };

  return (
    <div>
      <h2>Tutor Registration Form</h2>
      <form onSubmit={handleSubmit}>

        {/* Basic Information */}
        <h3>Basic Information <span className="required">*</span></h3>
        <div>
          <label>Name <span className="required">*</span>:</label>
          <input 
            type="text" 
            name="name" 
            value={tutorData.name} 
            onChange={handleChange} 
            required 
            placeholder="e.g., John Doe" 
          />
          <small>Please enter your full name.</small>
        </div>
        <div>
          <label>Phone <span className="required">*</span>:</label>
          <input 
            type="tel" 
            name="phone" 
            value={tutorData.phone} 
            onChange={handleChange} 
            required 
            placeholder="e.g., +1234567890" 
          />
          <small>Enter a valid phone number.</small>
        </div>
        <div>
          <label>Email <span className="required">*</span>:</label>
          <input 
            type="email" 
            name="email" 
            value={tutorData.email} 
            onChange={handleChange} 
            required 
            placeholder="e.g., johndoe@example.com" 
          />
        </div>
        <div>
          <label>Address:</label>
          <input 
            type="text" 
            name="address" 
            value={tutorData.address} 
            onChange={handleChange} 
            placeholder="e.g., 123 Main St." 
          />
        </div>
        <div>
          <label>Location <span className="required">*</span>:</label>
          <input 
            type="text" 
            name="location" 
            value={tutorData.location} 
            onChange={handleChange} 
            required 
            placeholder="e.g., New York, USA" 
          />
        </div>

        {/* Qualifications */}
        <h3>Qualifications <span className="required">*</span></h3>
        <div>
          <label>Higher Education:</label>
          <select name="higherEducation" value={tutorData.higherEducation} onChange={handleChange}>
            <option value="">Select Degree</option>
            <option value="Masters">Masters</option>
            <option value="PhD">PhD</option>
          </select>
        </div>
        <div>
          <label>
            <input type="checkbox" onChange={toggleBachelor} /> Add Bachelor Degree
          </label>
          {tutorData.bachelor !== '' && (
            <input 
              type="text" 
              name="bachelor" 
              value={tutorData.bachelor} 
              onChange={handleChange} 
              placeholder="e.g., BSc in Computer Science" 
            />
          )}
        </div>
        <div>
          <label>Experience (years) <span className="required">*</span>:</label>
          <input 
            type="number" 
            name="experience" 
            value={tutorData.experience} 
            onChange={handleChange} 
            required 
            placeholder="e.g., 5" 
          />
        </div>

        {/* Specializations */}
        <h3>Specializations <span className="required">*</span></h3>
        <div>
          <label>Subjects <span className="required">*</span>:</label>
          <select name="subjects" multiple={true} value={tutorData.subjects} onChange={addSubject}>
            <option value="Math">Math</option>
            <option value="Science">Science</option>
            <option value="English">English</option>
            <option value="History">History</option>
          </select>
        </div>
        <div>
          <label>Grade Levels <span className="required">*</span>:</label>
          <input 
            type="text" 
            name="gradeLevels" 
            value={tutorData.gradeLevels} 
            onChange={handleChange} 
            required 
            placeholder="e.g., High School, College" 
          />
        </div>

        {/* Availability */}
        <h3>Availability <span className="required">*</span></h3>
        <div>
          <label>Available From <span className="required">*</span>:</label>
          <input 
            type="date" 
            name="scheduleFrom" 
            value={tutorData.scheduleFrom} 
            onChange={handleChange} 
            required 
          />
        </div>
        <div>
          <label>Available Until <span className="required">*</span>:</label>
          <input 
            type="date" 
            name="scheduleUntil" 
            value={tutorData.scheduleUntil} 
            onChange={handleChange} 
            required 
          />
        </div>
        <div>
          <label>Mode of Tutoring <span className="required">*</span>:</label>
          <select 
            name="modeOfTutoring" 
            value={tutorData.modeOfTutoring} 
            onChange={handleChange} 
            required
          >
            <option value="">Select mode</option>
            <option value="in-person">In-person</option>
            <option value="online">Online</option>
            <option value="both">Both</option>
          </select>
        </div>

        {/* Additional Information */}
        <h3>Additional Information</h3>
        <div>
          <label>Tutoring Approach:</label>
          <textarea 
            name="tutoringApproach" 
            value={tutorData.tutoringApproach} 
            onChange={handleChange} 
            placeholder="Describe your teaching style and methods" 
          />
        </div>
        <div>
          <label>Rates (per hour):</label>
          <input 
            type="number" 
            name="rates" 
            value={tutorData.rates} 
            onChange={handleChange} 
            placeholder="e.g., 50" 
          />
        </div>
        <div>
          <label>Reviews/References:</label>
          <textarea 
            name="reviews" 
            value={tutorData.reviews} 
            onChange={handleChange} 
            placeholder="Any testimonials from past students or parents" 
          />
        </div>

        {/* Optional Information */}
        <h3>Optional Information</h3>
        <div>
          <label>Additional Skills:</label>
          <textarea 
            name="additionalSkills" 
            value={tutorData.additionalSkills} 
            onChange={handleChange} 
            placeholder="List any other relevant skills" 
          />
        </div>
        <div>
          <label>Profile Picture:</label>
          <input type="file" name="profilePicture" onChange={handleChange} />
        </div>

        {/* Consent */}
        <h3>Consent <span className="required">*</span></h3>
        <div>
          <label>
            <input 
              type="checkbox" 
              name="consent" 
              checked={tutorData.consent} 
              onChange={handleChange} 
              required 
            /> I agree to share my information on this platform.
          </label>
        </div>

        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default TutorRegistration;
