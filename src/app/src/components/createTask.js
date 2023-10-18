import { useState } from "react";

import { createTask } from "../services/APIService";
import CreateTaskForm from "./createTaskForm";

export default function CreateTask(props) {
  const [task, setTask] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    createTask({
      task: task,
      refreshCallback: props.refreshCallback,
      setTaskCallback: setTask,
    });

  };
  
  return (
    <div>
      <h1>Create a todo</h1>
      <CreateTaskForm
        task={task}
        handleSubmitCallback={handleSubmit}
        setTaskCallback={setTask}
      />
    </div>
  );
}
