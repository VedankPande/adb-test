import { useState } from "react";
import axios from "axios";

export default function CreateTask(props) {
    const [task, setTask] = useState("")

    const handleSubmit = async (e)=>{
        e.preventDefault()

        axios.post("http://localhost:8000/todos/",{
            task: task
        }).then((response)=>{
            setTask("")
            props.refreshCallback()
        }).catch((error)=>{
            alert(error.message)
            setTask("")
        })
        
    }
    return (
    <form onSubmit={handleSubmit}>
        <input 
        type="text"
        placeholder="Enter task to create"
        value={task}
        onChange={(e)=> setTask(e.target.value)}
        />
        <button type="submit">Create Item</button>
    </form>
    );
}
