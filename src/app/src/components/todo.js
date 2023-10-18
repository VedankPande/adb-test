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
        <CreateTask refreshCallback = {refreshData}/>
        <TaskList refresh = {refresh}/>
    </div>
  );
}
