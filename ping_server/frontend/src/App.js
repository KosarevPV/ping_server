import React from 'react';
import './App.css';
import {BrowserRouter, Route, Switch} from "react-router-dom";

import ResponseList from  "./components/Response";



class App extends React.Component {
    constructor(props) {
    super(props);
    this.state = { domains: [], responses: []};
    this.loadData = this.loadData.bind(this);
    }


    async loadData() {
        try {
            const domains_res = await fetch('http://127.0.0.1:8000/api/domains/');
            const responses_res = await fetch('http://127.0.0.1:8000/api/responses/');
            const domains_data = await domains_res.json();
            const responses_data = await responses_res.json();
            this.setState({
                domains: domains_data,
                responses: responses_data
            })
        } catch (e) {
            console.log(e);
        }
      }
        

    componentDidMount() {
        this.loadData()
        setInterval(this.loadData, 30000)
    };

    render () {
        return (
       <div>
            <BrowserRouter>
                <main>
                    <div>
                        <Switch>
                            <Route exact path='/chart' component={() =>
                                <ResponseList domains={this.state.domains} responses={this.state.responses}
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
