import { useState, useEffect } from "react";

import { getTasks } from "../services/APIService";

const useTodos = ({ refresh }) => {
  const [todo, setTodo] = useState(null);

  useEffect(() => {
    getTasks({ setTodoCallback: setTodo });
  }, [refresh]);

  return todo;
};

export default useTodos;
