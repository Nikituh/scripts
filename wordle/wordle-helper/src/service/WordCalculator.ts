
export class IndexedLetters {
	index!: number;
	letters?: string[];
}

export default class WordCalculator {

	private static words: string[];

	private static correctLetters: IndexedLetters[] = [];
	private static presentLetters: IndexedLetters[] = [];
	private static missingLetters: string[] = [];

	static async initialize(): Promise<void> {
		const response = await fetch("data/et_5words.txt");
		const text = await response.text();
		this.words = text.split("\n")
	}

	static doesNotContain(list: string[], letter: string): boolean {
		return !list.includes(letter);
	}

	static containsAtIndex(list: string[], letter: string, index: number): boolean {
		return list[index] === letter;
	}

	static containsButNotAtIndex(list: string[], letter: string, index: number): boolean {
		return list.includes(letter) && list[index] !== letter;
	}
	static updateCorrectLetters(index: number, letters: string[]) {
		const existing = this.correctLetters.find((letter) => letter.index === index)
		if (existing) {
			existing.letters = letters;
			return
		}
		this.correctLetters.push({ index, letters });
	}

	static updatePresentLetters(index: number, letters: string[]) {
		const existing = this.presentLetters.find((letter) => letter.index === index)
		if (existing) {
			existing.letters = letters;
			return
		}
		this.presentLetters.push({ index, letters });
	}

	static updateMissingLetters(letters: string[]) {
		this.missingLetters = letters;
	}

	static findRemainingWords() {
		const filtered: string[] = [];

		this.words.forEach((word: string) => {
			const letters = word.split("");

			const max_letters = 5;

			let isValidWord = false;

			for (let i = 0; i < max_letters; i++) {
				const il = this.correctLetters[i];
				if (!il || !il.letters) {
					continue;
				}
				il.letters!.forEach((letter) => {
					if (WordCalculator.containsAtIndex(letters, letter, il.index)) {
						isValidWord = true
					}
				});
			}

			if (isValidWord) {
				filtered.push(word);
			}

			
		});

		return filtered
	}
}