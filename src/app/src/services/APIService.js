import axios from "axios";

function createTask({ task, refreshCallback, setTaskCallback }){
    axios
    .post("http://localhost:8000/api/v1/todos/", {
      task: task,
    })
    .then((response) => {
      setTaskCallback("");
      refreshCallback();
    })
    .catch((error) => {
      alert(error.message);
      setTaskCallback("");
    });
}

async function getTasks({ setTodoCallback }){
    const res = await axios.get("http://localhost:8000/api/v1/todos/");
    const data = res.data.map((task) => JSON.parse(task));
    setTodoCallback(data);
}
export { createTask, getTasks }