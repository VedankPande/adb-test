
export default function TaskItem(props){
    return (
        <div key={props._id}>{props.task.task}</div>
    )
}