
import React from "react";

export default class RemainingWordGallery extends React.Component<any, any> {
    
    override render(): React.ReactNode {
        
        console.log("remaining words", this.props.words);
        
        return (
            <div style={{display: "flex", width: 200}}>
                {this.props.words.map((word: string) => {
                    return <div>{word}</div>
                })}
            </div>
        )
    }
}