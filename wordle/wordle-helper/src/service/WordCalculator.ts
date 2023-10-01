
export default class WordCalculator {
    
    static words: string[];

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

}