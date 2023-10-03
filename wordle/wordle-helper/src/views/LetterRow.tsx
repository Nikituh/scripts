import React from "react";
import LetterBox from "./LetterBox";

export default class LetterRow extends React.Component<any, any> {

    override render(): React.ReactNode {

        return (
            <div style={{...this.props.style, display: "flex"}}>
                {Array(5).fill(1).map((el, i) =>
                    <LetterBox key={i} index={i} color={this.props.color} onChange={this.props.onLetterChange} />
                )}
            </div>
        )
    }
}