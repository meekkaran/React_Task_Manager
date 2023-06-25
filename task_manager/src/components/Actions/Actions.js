import React from 'react'
import './actions.css';

const Actions = () => {
 return (
   <div className = "action_container">
        <div className= "action_items">
            <span>Priority</span>
            <button>Medium</button>
        </div>
        <div className= "action_items">
            <span>Due Date</span>
            <button>Date picker</button>
        </div>
        <div className= "action_items">
            <span>Tags</span>
            <button>Meetings</button>
            <button>UI Design</button>
            <button>UX Research</button>
            <button>Development</button>
        </div>
   </div>
   
 );
};

export default Actions;