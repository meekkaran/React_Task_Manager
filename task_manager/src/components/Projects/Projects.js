import React, { useState } from 'react';
import './projects.css';

// usestate is a react hook used to manage state of input field(task)

function Projects() {
  const [task, setTask] = useState('');
  const [todoTasks, setTodoTasks] = useState([]);
  const [doneTasks, setDoneTasks] = useState([]);

// funct handlechage updates 'task' state asone inputs task in input field
  const handleChange = (event) => {
    setTask(event.target.value);
  };

 // handlecreatetask - this is called when button create task is clicked - it adds task to list of tasks
  const handleCreateTask = () => {
    if (task !== '') {
      setTodoTasks([...todoTasks, task]);
      setTask(''); //reset state
    }
  };

  // handlemovetodone triggers done which  removes tasks from todo to done
  const handleMoveToDone = (index) => {
    const newTodoTasks = [...todoTasks];
    const taskToMove = newTodoTasks.splice(index, 1)[0];
    setTodoTasks (newTodoTasks);  //update todotask state with modified array
    setDoneTasks([...doneTasks, taskToMove]);
  };

  return (
    <div className='container'>
      <h1>Todo List</h1>
      <div className='input-container'>
        <input type="text" value={task} onChange={handleChange} />
        <button onClick={handleCreateTask}>Create Task</button>
      </div>

      <div className='todo-container'>
        <h2>Todo</h2>
        {todoTasks.map((task, index) => (
          <div className='task-item' key={index}>
            <span>{task}</span>
            <button onClick={() => handleMoveToDone(index)}>Done</button>
          </div>
        ))}
      </div>
      <div className='done-container'>
        <h2>Done</h2>
        {doneTasks.map((task, index) => (
          <div className='task-item done' key= {index}>
            <span>{task}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Projects;
