import React from 'react';
import WordCalculator from './service/WordCalculator';
import LetterRow from './views/LetterRow';
import Colors from './utils/colors';
import LetterBox from './views/LetterBox';
import Size from './utils/size';

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

	onCorrectLetterChange(index: number, letters: string[]) {
		console.log("onCorrectLetterChange", index, letters);
	}

	onPresentLetterChange(index: number, letters: string[]) {
		console.log("onPresentLetterChange", index, letters)
	}

	onMissingLetterChange(index: number, letters: string[]) {
		console.log("onMissingLetterChange", letters)
	}

	override render(): React.ReactNode {

		// Calculation contains an extra -margin to account for text padding inside the input
		const rowWidth = 5 * (Size.LetterBoxWidth + Size.LetterBoxMargin) - 2 * Size.LetterBoxMargin;

		return (
			<div style={{
				display: "flex",
				flexDirection: "column",
				alignItems: "center",
				height: "100vh",
				width: "100vw",
				paddingTop: 100
			}}>
				<LetterRow color={Colors.Correct} onLetterChange={this.onCorrectLetterChange} />
				<div style={{ height: 5 }}></div>
				<LetterRow color={Colors.Present} onLetterChange={this.onPresentLetterChange} />
				<div style={{ height: 5 }}></div>
				<LetterBox color={Colors.Missing} width={rowWidth} onChange={this.onMissingLetterChange} />
			</div>
		);
	}

}


