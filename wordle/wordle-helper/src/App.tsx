import React from 'react';
import WordCalculator from './service/WordCalculator';
import LetterRow from './views/LetterRow';
import Colors from './utils/colors';
import LetterBox from './views/LetterBox';
import Size from './utils/size';
import RemainingWordGallery from './views/RemainingWordGallery';

export default class App extends React.Component<any, any> {

	constructor(props: any) {
		super(props);
		this.state = {
			words: []
		}
	}

	override async componentDidMount(): Promise<void> {

		await WordCalculator.initialize();
	}

	onCorrectLetterChange(index: number, letters: string[]) {
		WordCalculator.updateCorrectLetters(index, letters);
		this.setState({ words: WordCalculator.findRemainingWords() });
	}

	onPresentLetterChange(index: number, letters: string[]) {
		WordCalculator.updatePresentLetters(index, letters);
		this.setState({ words: WordCalculator.findRemainingWords() });
	}

	onMissingLetterChange(index: number, letters: string[]) {
		WordCalculator.updateMissingLetters(letters);
		this.setState({ words: WordCalculator.findRemainingWords() });
	}

	override render(): React.ReactNode {

		// Calculation contains an extra -margin to account for text padding inside the input
		const rowWidth = 5 * (Size.LetterBoxWidth + Size.LetterBoxMargin) - Size.LetterBoxMargin;

		return (
			<div style={{
				display: "flex",
				flexDirection: "column",
				alignItems: "center",
				height: "100vh",
				width: "100vw",
				paddingTop: 100,
				backgroundColor: Colors.NavyBackground
			}}>
				<LetterRow color={Colors.Correct} onLetterChange={this.onCorrectLetterChange.bind(this)} style={{paddingBottom: 5}} />
				<LetterRow color={Colors.Present} onLetterChange={this.onPresentLetterChange.bind(this)}  style={{paddingBottom: 5}} />
				<LetterBox color={Colors.NavyBox} width={rowWidth} onChange={this.onMissingLetterChange.bind(this)} />
				<RemainingWordGallery words={this.state.words}/>
			</div>
		);
	}

}


