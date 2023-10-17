import { useState, useEffect } from "react";
import TaskList from "./taskList";
import CreateTask from "./createTask";

export default function Todo() {
  const [refresh, setRefresh] = useState(false);

  const refreshData = ()=>{
    setRefresh(!refresh)
  }

  return (
    <div className="App">
        <>
          <h1> List of Todos </h1>
          <TaskList refresh = {refresh}/>
          <h1> Create a Todo </h1>
          <CreateTask refreshCallback = {refreshData}/>
        </>
    </div>
  );
}
