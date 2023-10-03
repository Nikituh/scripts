
import React from "react";
import Size from "../utils/size";

export default class LetterBox extends React.Component<any, any> {

    override render(): React.ReactNode {

        const size = Size.LetterBoxWidth;

        return (
            <input
                style={{
                    // Calculation contains an extra -margin to account for text padding inside the input
                    width: this.props.width ?? size,
                    height: size,
                    marginRight: Size.LetterBoxMargin,
                    backgroundColor: this.props.color,
                    border: "none",
                    fontSize: 20,
                    lineHeight: size + "px",
                    color: "white",
                    padding: 0,
                    borderRadius: 5,
                    textAlign: "center"
                }}
                type="text"
                onChange={(e) => {
                    const value = e.target.value;
                    const letters = value.split("");
                    this.props.onChange(this.props.index, letters);
                }}
            />
        )
    }
}