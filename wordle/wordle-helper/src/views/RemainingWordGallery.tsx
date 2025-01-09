
import React from "react";

export default class RemainingWordGallery extends React.Component<any, any> {

    override render(): React.ReactNode {

        const words = this.props.words.length > 99 ? this.props.words.slice(0, 99) : this.props.words;
        if (words.length === 0) {
            return null;
        }

        if (this.props.words.length > 99) {
            words.push("...");
        }
        
        return (
            <div style={{ display: "flex", flexWrap: "wrap", width: 400, paddingTop: 20, overflow: "scroll", }}>
                {words.map((word: string) => {
                    return <div
                        key={word}
                        style={{
                            display: "flex",
                            justifyContent: "center",
                            alignItems: "center",
                            flexBasis: "20%",
                            paddingBottom: 3,
                            color: "white",
                        }}
                    >{word}</div>
                })}
            </div>
        )
    }
}