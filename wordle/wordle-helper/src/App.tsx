import React from 'react';

export default class App extends React.Component<any, any> {

	override async componentDidMount(): Promise<void> {
		const response = await fetch("data/et_5words.txt");
		const text = await response.text();
		const words = text.split("\n")
		console.log("words", words);
	}

	override render(): React.ReactNode {
		return (
			<div>

			</div>
		);
	}

}
