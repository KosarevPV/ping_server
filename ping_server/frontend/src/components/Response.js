import React from 'react'

const ResponseItem = ({domain_name, domain_id, responses}) => {
    const arr_responses = responses.filter(el => el.domain === domain_id).map(el => `${el.responses_time} / `)
    return (
        <tr>
            <td>{domain_name}</td>
            <td>{arr_responses}</td>
        </tr>
    )
}


export const ResponseList = ({domains, responses}) => {

    return (
        <div>
            <table>
                <tr>
                    <th>Domain</th>
                    <th>Response time</th>
                </tr>
                {domains.map((item) => <ResponseItem domain_name={item.domain_name} domain_id={item.id} responses={responses}/>)}
            </table>
        </div>

    )
}


export default ResponseList