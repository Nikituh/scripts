
import React from "react";

export default class RemainingWordGallery extends React.Component<any, any> {
    
    override render(): React.ReactNode {
        
        console.log("remaining words", this.props.words);

        return (
            <div style={{display: "flex", flexWrap: "wrap", maxWidth: 400, paddingTop: 20}}>
                {this.props.words.map((word: string) => {
                    return <div
                        style={{
                            display: "flex",
                            justifyContent: "center",
                            alignItems: "center",
                            flexBasis: "20%",
                            paddingBottom: 3
                        }}
                    >{word}</div>
                })}
            </div>
        )
    }
}