import React from 'react';
import WordCalculator from './utils/WordCalculator';

export default class App extends React.Component<any, any> {

	override async componentDidMount(): Promise<void> {

		await WordCalculator.initialize();

		const filtered: string[] = [];

		WordCalculator.words.forEach((word: string) => {
			const letters = word.split("");
			if (
				WordCalculator.containsAtIndex(letters, "k", 2) &&
				WordCalculator.containsAtIndex(letters, "t", 4) &&
				WordCalculator.containsButNotAtIndex(letters, "k", 0) &&
				WordCalculator.containsButNotAtIndex(letters, "t", 3) &&
				WordCalculator.doesNotContain(letters, "o") &&
				WordCalculator.doesNotContain(letters, "h") &&
				WordCalculator.doesNotContain(letters, "u")
			) {
				filtered.push(word);
			}
		});

		console.log("filtered words", filtered);
	}

	override render(): React.ReactNode {
		return (
			<div>

			</div>
		);
	}

}


