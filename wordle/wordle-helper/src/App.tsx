import React from 'react';

export default class App extends React.Component<any, any> {

	doesNotContain(list: string[], letter: string) {
		return !list.includes(letter);
	}

	containsAtIndex(list: string[], letter: string, index: number): boolean {
		return list[index] === letter;
	}

	containsButNotAtIndex(list: string[], letter: string, index: number): boolean {
		return list.includes(letter) && list[index] !== letter;
	}

	override async componentDidMount(): Promise<void> {
		const response = await fetch("data/et_5words.txt");
		const text = await response.text();
		const words = text.split("\n")

		const filtered: string[] = [];

		words.forEach((word: string) => {
			const letters = word.split("");
			if (
				this.containsAtIndex(letters, "a", 0) &&
				this.containsAtIndex(letters, "e", 3) &&
				this.containsButNotAtIndex(letters, "e", 1) &&
				this.containsButNotAtIndex(letters, "l", 1) &&
				this.doesNotContain(letters, "r") &&
				this.doesNotContain(letters, "u") &&
				this.doesNotContain(letters, "s") &&
				this.doesNotContain(letters, "t") &&
				this.doesNotContain(letters, "g")
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


