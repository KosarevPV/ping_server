import React from 'react';
import axios from 'axios';
import './App.css';
import {BrowserRouter, Route, Switch} from "react-router-dom";

import ResponseList from  "./components/Response";



class App extends React.Component {
    constructor(props) {
    super(props)
        this.state = {
            data: {
                labels: [],
                datasets: [],
              },
        }
    }

    componentDidMount() {
    //     axios.get('http://127.0.0.1:8000/api/domains/')
    //                 .then(response => {
    //                     this.setState(
    //                         {
    //                             data: response.data
    //                         }
    //                     )}).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/domains/')
            .then(response => {
                let domains = response.data
                domains.map((domain) => (
                    axios.get(`http://127.0.0.1:8000/api/responses_f/?domain=${domain.id}`)
                    .then(response => { 
                        let res_domain = response.data
                        let values = res_domain.map((item) => item.responses_time)
                        
                        if (this.state.data['labels'].length < ((Math.ceil((values.length/6)+1))*6)) {
                            for(var i=this.state.data['labels'].length;i<((Math.ceil((values.length/6)+1))*6);i++){
                                this.state.data['labels'].push(i);
                            }
                        }

                        if (this.state.data['datasets'].find((item) => item.label === domain.domain_name) === undefined) {
                            this.state.data['datasets'].push({
                                label: domain.domain_name,
                                data: values,  
                            })
                        }                 
                    }
                    )
                )
                )
            }).catch(error => console.log(error))
    };

    render () {
        return (
       <div>
            <BrowserRouter>
                <main>
                    <div>
                        <Switch>
                            <Route exact path='/chart' component={() =>
                                <ResponseList data={this.state.data}
                                />}/>
                        </Switch>
                    </div>
                </main>
            </BrowserRouter>
       </div>
        )
    }

}

export default App;
