import React from 'react'

const ResponseItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.repoUrl}</td>
            <td>{project.users}</td>
            <td>
                <button onClick={() => deleteProject(project.id)}
                        type='button'>Delete
                </button>
            </td>
        </tr>
    )
}


export const ResponseList = ({data}) => {
    console.log(data.labels)
    return (
        <div>
            <table>
                <tr>
                    <th>Domain</th>
                    <th>Response time</th>
      
                    <th></th>
                </tr>
            </table>
        </div>

    )
}


export default ResponseList