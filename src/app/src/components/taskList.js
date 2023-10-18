import useTodos from "../hooks/useTodos";
import TaskItem from "./taskItem";

export default function TaskList(props) {
  //custom hook to fetch all todos
  const todos = useTodos({
    refresh: props.refresh,
  });

  return (
    <div>
      <h1>List of todos</h1>
      {todos && (
        <div>
          {todos.map((task) => (
            <TaskItem task={task} />
          ))}
        </div>
      )}
    </div>
  );
}
