export default function CreateTaskForm(props){

    return(
        <form onSubmit={props.handleSubmitCallback}>
        <input
          type="text"
          placeholder="Enter task to create"
          value={props.task}
          onChange={(e) => props.setTaskCallback(e.target.value)}
        />
        <button type="submit">Create Item</button>
      </form>
    )
}