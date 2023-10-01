
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

			if (this.containsAllLettersAtCorrectIndices(word) && this.containsAllPresentLettersNotAtIndices(word) && this.doesNotContainMissingLetters(word)) {
				filtered.push(word);
			}
		});

		return filtered
	}

	static containsAllLettersAtCorrectIndices(word: string): boolean {
		const letters = word.split("");

		const max_letters = 5;

		for (let i = 0; i < max_letters; i++) {
			const il = this.correctLetters[i];
			if (!il || !il.letters) {
				continue;
			}

			for (let j = 0; j < il.letters.length; j++) {
				if (!WordCalculator.containsAtIndex(letters, il.letters[j], il.index)) {
					return false;
				}
			}
		}

		return true;
	}

	static containsAllPresentLettersNotAtIndices(word: string): boolean {
		
		const letters = word.split("");

		const max_letters = 5;

		for (let i = 0; i < max_letters; i++) {
			const il = this.presentLetters[i];
			if (!il || !il.letters) {
				continue;
			}
			for (let j = 0; j < il.letters.length; j++) {
				if (!WordCalculator.containsButNotAtIndex(letters, il.letters[j], il.index)) {
					return false;
				}
			}
		}

		return true;
	}

	static doesNotContainMissingLetters(word: string): boolean {
		const letters = word.split("");

		return this.missingLetters.every((letter) => {
			return WordCalculator.doesNotContain(letters, letter);
		});
	}

}