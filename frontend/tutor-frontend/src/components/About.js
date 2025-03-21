import React from 'react';
import '../styles/About.css'; // Separate CSS for About section

function About() {
  return (
    <div className="about-container">
      <h2>About Tutor Finder</h2>
      <p>
        Tutor Finder is a platform designed to connect students with qualified tutors across a wide range of subjects. Our goal is to make education accessible and personalized by offering a simple way for tutors and students to connect.
      </p>
      <p>
        Whether you're a student looking to improve your grades, prepare for exams, or expand your knowledge, Tutor Finder offers a diverse selection of tutors who can meet your individual needs. Our platform allows tutors to easily register and manage their profiles while helping students find the perfect tutor based on their specialization and location.
      </p>
      <h3>Our Mission</h3>
      <p>
        Our mission is to bridge the gap between students and qualified educators by providing a reliable, user-friendly platform where learning is personalized, flexible, and accessible to everyone. We believe that education should be available to all, and we are committed to supporting learners of all ages and levels.
      </p>
      <h3>How It Works</h3>
      <ul>
        <li>Register as a tutor or student on our platform.</li>
        <li>Search for tutors based on subjects, grade levels, and availability.</li>
        <li>Interact with our intelligent chatbot for more information or assistance.</li>
        <li>Connect with tutors for online or in-person sessions.</li>
      </ul>
      <h3>Why Choose Us?</h3>
      <ul>
        <li>Wide range of qualified tutors across various subjects.</li>
        <li>Flexible scheduling options for both tutors and students.</li>
        <li>Simple, easy-to-use interface with chatbot assistance.</li>
        <li>Personalized learning experience tailored to each student’s needs.</li>
      </ul>
      <p>
        At Tutor Finder, we are committed to improving the way students and educators interact, making learning more accessible and effective for everyone.
      </p>
    </div>
  );
}

export default About;
