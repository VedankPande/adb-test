import { useState, useEffect } from "react";
import axios from "axios";

export default function TaskList(props) {
  const [loading, setLoading] = useState(true);
  const [todoData, setTodoData] = useState(null);

  const fetchData = async (url) => {
    const res = await axios.get(url);
    const data = res.data.map((task) => JSON.parse(task));
    setTodoData(data);
    setLoading(false);
  };

  useEffect(async () => {
    console.log("useEffect in taskList");
    fetchData("http://localhost:8000/todos/");
  }, [props.refresh]);

  return (
    <div>
      {todoData &&
        (loading ? (
          "Loading"
        ) : (
          <div>
            {todoData.map((task) => (
              <div key={task._id}>{task.task}</div>
            ))}
          </div>
        ))}
    </div>
  );
}
