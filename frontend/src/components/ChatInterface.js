import React from "react";
import axios from 'axios';


class ChatInterface extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            context: [
                {'system': ''},
            ],
            prompt: "",
        }
    }

    fetchContext = (context) => {
        this.setState({
            context: context,
        });
    }

    updateContext = (prompt, agent) => {
        let context = [...this.state.context];
        if(agent === 'user'){
            context.push({'user': prompt});
        } else {
            context.push({'assistant': prompt});
        }

        this.setState({
            context: context
        })
    } 

    fetchChatResponse = (event) => {
        event.preventDefault();
        const prompt = this.state.prompt;
        console.log(prompt)
        let objContext = {...this.state.context};
        let context = objContext.context;
        // context.push({'user': prompt});
        // this.setState({
        //     context: context
        // })
        // console.log(context)
        axios.post('http://127.0.0.1:5000/', {
            prompt: prompt,
            context: context,
        }).then((response) =>{
            console.log(`POST SUCCESS`, response.data);
            this.setState({
                context: response?.data,
                prompt: ""
            })
        }).catch(error => console.log(error));
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:5000/').then(response => {
            console.log("SUCCESS", response.data)
            this.fetchContext(response.data);
            // console.log(response);
            }).catch(error => {
            console.log(error)
        })
    }

    render() {
        return <>
            {/* <img src="{{ url_for('static', filename='dog.png') }}" class="icon" /> */}
            <h3>Ask Anything to FitJoe</h3>
            <form>
                <input 
                type="text"  
                value={this.state.prompt}
                onChange={(e) => this.setState({prompt: e.target.value})} 
                placeholder="Enter your prompt" required />
                <input type="submit" onClick={this.fetchChatResponse} />
            </form>

            <ul className="convo">
                {Array.isArray(this.state.context.context) ? this.state.context.context.map((cntx, idx) => {
                    const role = cntx['role'];
                    const dialogue = cntx['content'];
                    console.log(role, dialogue, idx)
                    if(role==='user')
                        return <li className="dialogues" key={idx}>User: {dialogue} <br /></li>
                    else if(role==='assistant')
                        return <li className="dialogues" key={idx}>FitJoe: {dialogue} <br /></li>
                    return<></>;
                }) : <></>}
            </ul>
        </>
    }
}

export default ChatInterface;