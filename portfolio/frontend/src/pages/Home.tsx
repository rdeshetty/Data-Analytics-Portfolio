import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { getExperiences, getSkills, getEducation, Experience, Skill, Education } from '../services/api';

const Home = () => {
  const [experiences, setExperiences] = useState<Experience[]>([]);
  const [skills, setSkills] = useState<Skill[]>([]);
  const [education, setEducation] = useState<Education[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [expData, skillsData, eduData] = await Promise.all([
          getExperiences(),
          getSkills(),
          getEducation(),
        ]);
        setExperiences(expData);
        setSkills(skillsData);
        setEducation(eduData);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  // Group skills by category
  const skillsByCategory = skills.reduce<Record<string, Skill[]>>((acc, skill) => {
    if (!acc[skill.category]) {
      acc[skill.category] = [];
    }
    acc[skill.category].push(skill);
    return acc;
  }, {});

  return (
    <div className="bg-gray-50">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary-600 to-primary-800 text-white py-20">
        <div className="section-container">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-center"
          >
            <h1 className="text-4xl md:text-6xl font-bold mb-4">
              Rishikesh Deshetty
            </h1>
            <p className="text-xl md:text-2xl mb-2">Data Analyst | IT Professional</p>
            <p className="text-lg md:text-xl mb-8 text-primary-100">
              Minneapolis, MN | rishikesh.d1020@gmail.com | (818) 930-4585
            </p>
            <div className="flex flex-col sm:flex-row justify-center gap-4">
              <a href="#contact" className="btn-primary bg-white text-primary-600 hover:bg-gray-100">
                Get In Touch
              </a>
              <a href="/Rishikesh_Deshetty_Resume.pdf" download className="btn-secondary border-white text-white hover:bg-white hover:text-primary-600">
                Download Resume
              </a>
            </div>
          </motion.div>
        </div>
      </section>

      {/* About Section */}
      <section className="section-container">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
        >
          <h2 className="section-title">About Me</h2>
          <div className="max-w-4xl mx-auto">
            <div className="card">
              <p className="text-lg text-gray-700 leading-relaxed mb-4">
                Data Analyst with <strong>3+ years of experience</strong> in data analytics, consulting support, 
                and business operations within healthcare and retail domains. Adept at translating business needs 
                into analytical insights, supporting decision-making through data validation, and collaborating 
                across global teams.
              </p>
              <p className="text-lg text-gray-700 leading-relaxed">
                Skilled in leveraging tools such as <strong>Excel, Power BI, Tableau, SQL, and Python</strong> to 
                deliver accurate, actionable insights that improve performance and operational efficiency. Passionate 
                about continuous learning, stakeholder communication, and creating measurable impact in fast-paced 
                environments.
              </p>
            </div>
          </div>
        </motion.div>
      </section>

      {/* Education Section */}
      <section className="section-container bg-white">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
        >
          <h2 className="section-title">Education</h2>
          <div className="max-w-4xl mx-auto space-y-6">
            {education.map((edu) => (
              <div key={edu.id} className="card">
                <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-2">
                  <div>
                    <h3 className="text-xl font-bold text-gray-900">{edu.institution}</h3>
                    <p className="text-lg text-primary-600 font-semibold">
                      {edu.degree} in {edu.field_of_study}
                    </p>
                  </div>
                  <div className="text-right mt-2 md:mt-0">
                    <p className="text-gray-600">{edu.location}</p>
                    <p className="text-gray-600">{edu.graduation_date}</p>
                  </div>
                </div>
                <p className="text-gray-700">
                  <strong>GPA:</strong> {edu.gpa}
                </p>
              </div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* Experience Section */}
      <section className="section-container">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
        >
          <h2 className="section-title">Professional Experience</h2>
          <div className="max-w-4xl mx-auto space-y-8">
            {experiences.map((exp, index) => (
              <motion.div
                key={exp.id}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
                className="card"
              >
                <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-4">
                  <div>
                    <h3 className="text-2xl font-bold text-gray-900">{exp.position}</h3>
                    <p className="text-lg text-primary-600 font-semibold">{exp.company}</p>
                  </div>
                  <div className="mt-2 md:mt-0">
                    <span className="inline-block px-3 py-1 bg-primary-100 text-primary-800 rounded-full text-sm font-medium">
                      {exp.duration}
                    </span>
                    {exp.is_current && (
                      <span className="ml-2 inline-block px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-medium">
                        Current
                      </span>
                    )}
                  </div>
                </div>
                <div className="text-gray-700 whitespace-pre-line">
                  {exp.description}
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* Skills Section */}
      <section className="section-container bg-white">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
        >
          <h2 className="section-title">Technical Skills</h2>
          <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {Object.entries(skillsByCategory).map(([category, categorySkills]) => (
              <motion.div
                key={category}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
                viewport={{ once: true }}
                className="card"
              >
                <h3 className="text-xl font-bold text-gray-900 mb-4 flex items-center">
                  <span className="w-2 h-2 bg-primary-600 rounded-full mr-2"></span>
                  {category}
                </h3>
                <div className="space-y-3">
                  {categorySkills.map((skill) => (
                    <div key={skill.id}>
                      <div className="flex justify-between mb-1">
                        <span className="text-sm font-medium text-gray-700">{skill.name}</span>
                        <span className="text-sm text-gray-500">{skill.proficiency}%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div
                          className="bg-primary-600 h-2 rounded-full transition-all duration-500"
                          style={{ width: `${skill.proficiency}%` }}
                        ></div>
                      </div>
                    </div>
                  ))}
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* CTA Section */}
      <section className="section-container bg-gradient-to-r from-primary-600 to-primary-800 text-white">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
          className="text-center"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Let's Work Together
          </h2>
          <p className="text-xl mb-8 text-primary-100">
            I'm always open to discussing new projects and opportunities.
          </p>
          <a href="/contact" className="btn-primary bg-white text-primary-600 hover:bg-gray-100">
            Contact Me
          </a>
        </motion.div>
      </section>
    </div>
  );
};

export default Home;
