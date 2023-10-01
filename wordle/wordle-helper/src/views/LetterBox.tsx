
import React from "react";
import Size from "../utils/size";

export default class LetterBox extends React.Component<any, any> {

    override render(): React.ReactNode {

        const size = Size.LetterBoxWidth;

        return (
            <input style={{
                // Calculation contains an extra -margin to account for text padding inside the input
                width: this.props.width ?? (size - Size.LetterBoxMargin),
                height: size,
                marginRight: Size.LetterBoxMargin,
                backgroundColor: this.props.color,
                border: "none",
                fontSize: 20,
                lineHeight: size + "px",
                
                color: "white",
                padding: 0,
                borderRadius: 5,
                paddingLeft: Size.LetterBoxMargin,
            }} type="text" />
        )
    }
}