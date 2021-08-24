## Initial commit: Or, the struggle to get this site done.

### Introduction

Preface: Half of this post will just be rant of some random stuff, as I'm honestly just writing this as I build it. Writing down and hating on all manner of small inconveniences I counter. The other half should be fun.

As some of you may know, when it comes to web development (at least for more feature-intensive projects), React is my tool of choice. There are underlying performance that have shaped this opinion (virtual DOM update performance compared to Angular is out of this world), but the main reason actually is ease of development. 

I've never been much of a fan of the `html`, `css` and `js` as separate entities. I believe that will create a lot of confusion once the project gets out of the <Hello World> phase. Building separate components, where each component is a single file that manages its content and styling, works best for me. Maybe it's because I come from an OOP-based world, maybe it's Maybelline.

It is what it is.

So, I decide build a blog in React.

What do I do? I google "react blog", "react headless blog", "react blog template", "material blog template" and countless other variants. Honestly, I thought this part would be easier, but apparently there exist no simple blog templates that would fit my needs. Those being:

1. Lightweight
2. Headless (or at least what I thought headless meant -- serverless. I don't special storage or an admin panel. Let it just be a client that can load markdown from somewhere)
3. Modern and responsive. I'm by no means a designer, but I am human and I do enjoy pretty colors and animations

Not too difficult, right? Well, apparently it is, as I found nothing out there that would work for me (including minimal redesign and personalisation, of course). Then, screw it, we'll build it from scratch.

From scratch still being with React and Material-UI, naturally, I'm not a masochist. Vanilla html/js/css is fun, but not when accounting for ease of development, maintenance, responsive design, cross-browser compatibility etc. Well, it's basically good-for-nothing then, I suppose. 

Moving on...

### Laying the groundwork

#### Project

```
npx create-react-app blogging-molly --template typescript
```
Blogging Molly. Because you can't really make a blog pun with "Aare" or "Niki". Also because it's a throwback to a simpler time -- back when I was in high school and just discovering irish punk, and myself, I combined the two into my first blog.

And that's it. We have our template project. The boys at React have made it real freakin' simple to get started. 

As the next step, let's move all the nonsense from the project. Just completely nuke the following files: `App.css`, `App.test.tsx`, `logo.svg`, `react-app-env.d.ts`, `reportWebVitals.js` and `setupTests.ts`. Honestly, I have no idea why they decided to include a bunch of diagnostics and testing stuff in a sample project creator.

Approximately 90% of the people who use will not be writing tests for their simple sites, and the other 10% will remove the defaults anyway, as they probably have their own thing going on. 

#### Dependencies

Right off the bat, we'll add the dependencies we think we'll require. Always build the proof of concept before you get to styling. If the proof of concept is done, it's far simpler to tinker on the design in-between building the actual site.

```
"react-markdown": "5.0.3"
```

Right off the bat, let's add the core of the project. I've never used `react-markown` before, so let's hope it all works out.

```
"react-router-dom": "6.0.0-beta.0",
```

Add the router because even a basic blog site will have some navigation: moving from the list of posts to the content.

```
"@material-ui/core": "5.0.0-alpha.25",
```

Just for good measure, I'll add material right away as well. I know I'll need it anyway, so why wait.

And just added the latest bleeding edge alpa, because the material-ui team is not keeping up with the move-fast-and-breka-stuff guys.

Strict mode was deprecated in React some time ago, but Material v4 still makes use of, resulting in the following error (it says warning, but the color is error, so we know it's serious!):

```
Warning: findDOMNode is deprecated in StrictMode. findDOMNode was passed an instance of Transition which is inside StrictMode.
```

Argh. But right off the bat I'm seeing some trouble with the alpa version. It looks like the separately adding the following dependencies is now required:

```
"@emotion/react": "11.1.5",
"@emotion/styled": "11.1.5"
```

I have no idea what they are, or why they are necessary, but the error message was relatively straightforward, so let's just go with it.

#### Building the DOM

Right off the bat, let's clean our content entrypoint, `App.tsx`. I've always preferred class structure to functional components. No religious logic here, I just find it more readable. So:

```
import React from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      </header>
    </div>
  );
}

export default App;
```

Becomes:

```
import React from 'react';

export default class App extends React.Component<any, any> {

    render() {
        return (
            <div className="App">
                <header className="App-header">
      			</header>
            </div>
        );
    }
}
```

#### Testing Markdown parser

After the initial refactor, our `App.tsx` now becomes:

```

import React from 'react';
import ReactMarkdown from 'react-markdown';
import {Styles} from "./styles/Styles";

export default class App extends React.Component<any, any> {

    markdown: string = "A paragraph with *emphasis* and **strong importance**, but what about `code`, and what about ```code blocks```";

    render() {
        return (
            <div style={Styles.background}>
                <div style={Styles.post}>
                    <ReactMarkdown children={this.markdown}/>
                </div>
            </div>
        );
    }
}
```

`Styles` is just a basic style file I created just to add some dark styling, margins and center content. So far so good, seems to render the content exactly as I expected. Well, code blocks. Doesn't seem to handle newline characters quite either. But we'll need to load in this exact file to see how he handles that.

The following markdown:
```
markdown = "A paragraph with *emphasis* and **strong importance**. ```and code blocks```";
```

Gets rendered as the following image:

![Image](https://aare.dev/posts/images/1-1.first-test.png)

From [their own documentation](https://github.com/remarkjs/react-markdown), let's just add some code renderers and see how that turns out:

```
import {Prism as SyntaxHighlighter} from 'react-syntax-highlighter'
import {dark} from 'react-syntax-highlighter/dist/esm/styles/prism'
```

```
renderers = {
    // @ts-ignore
    code: ({language, value}) => {
        return <SyntaxHighlighter style={dark} language={language} children={value} />
    }
};
```

```
<ReactMarkdown renderers={this.renderers} plugins={[gfm]} children={this.markdown}/>
```

Damn. it somehow looks terrible, and somehow turns most of the content into code blocks, not just the parts I'm actually defining as code blocks.

The markdown now is:

```
    markdown = `A paragraph with *emphasis* and **strong importance**.

wut

    * Lists
    * [ ] todo
    * [x] done

    A table:
    emojiii  ✨
    | a | b |
    | - | - |

    fdgdg

    ~~~js
    console.log('It works!')
    ~~~~
    `;
```

And the resulting image is:

![Image](https://aare.dev/posts/images/1-2.renderers-test.png)


Well, it at least technically works. I'm sure we can figure out how to properly style it later on. Besides, we're not gonna be working with string markdown constants defined in code. Let's see how it handles files.


### Loading .md

Since React (and more specifically, `react-scripts`) changes up how assets are included all the damn time, I've given up on trying to understand it. Thing is, `react-scripts` uses webpack under the hood, and wraps it into an easy-to-understand package, but that also means it's barely configurable.

I'm not ready to `eject` `react-scripts` either and start configuring webpack manually right now so it would also load markdown. Instead, I propose a more straightforward solution:

Let's get one step ahead of them and just upload this markdown to a server right away and just fetch it back. I mean, eventually, posts should be stored separately anyway.

First, let's download the file. Since I have the domain and server ready, I just created a `posts` folder, slapped the file there and we're ready to go.

Luckily javascript offers a very convenient way to fetch files. Basically just a oneliner:

```
const result = await fetch("https://aare.dev/posts/initial-commit.md");
const text = await result.text();
```

Note that, for example, Google Chrome does block cross-origin resource sharing, meaning that I cannot request files from another server and display them. Mostly a security feature, in this annoying. There are various ways to disable these security features on different browsers. 

I have created an alias for me. Found that rather convenient. If I just type `chrdev`, it opens another instance of Chrome where I can fuck shit up.

The alias itself is (in `/Users/$USER/.zshrc`):

```
alias chrdev="open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security"
```

### Reactive programming

Before we move on to displaying the content, let's make our app pure reactive. That's just for good measure.

For example, a good place to load the mardown file would be in `componentDidMount`:

```
async componentDidMount(): Promise<void> {
    const result = await fetch("https://aare.dev/posts/initial-commit.md");
    const text = await result.text();
}
```

Let's also turn our `markdown` property into a state, so it can be neatly managed by react internally. Just override the constructor and define a default state. Initially, we want our markdown to be empty:

```
constructor(props: any) {
    super(props);

    this.state = {
        markdown: ""
    }
}
```

After requesting the file, simply update the state:
```
this.setState({markdown: text});
```

The `ReactMarkdown` virtual dom element should also use the `markdown` property of the `state`, not the global one:

```
<ReactMarkdown plugins={[gfm]} children={this.state.markdown}/>
```

And that's that. This entire file is displayed perfectly in the container we defined. Even code blocks, my main point of concern, are properly rendered. Woop! 🎉

However, some proper styling needs to be applied right away. Currently it's too ugly to even show an image of it. Ugh.

### Markdown Styling

Styling was, very surprisingly, very much easier than I had anticipated. With a little bit of googling around, I found the `github-markdown-css` [package](https://www.npmjs.com/package/github-markdown-css):

```
npm install github-markdown-css
```

Just import the entire thing:
```
import 'github-markdown-css'
```

And apply the body class to your markdown parent element:
```
<div style={Styles.post} className='markdown-body'>
    <ReactMarkdown plugins={[gfm]} children={this.state.markdown}/>
</div>
```

This works exactly like this because importing css forces (1) Webpack to include the file and (2) React to apply the file when rendering the page. 

Essentially it works exactly like loading the CSS in the `head` of your `index.html`. If it's loaded, it's applied.

The outcome is as follows:

![Image](https://aare.dev/posts/images/1-3.github-styled.png)

### Accessorizing

The markdown is perfect, but the site itself still looks relatively bland. I think we could fix that with a navigation bar.

First, I needed to think of the perfect header text for the blog, but since I'm pretty sick of it already, this one will do:

```
TITLE = "aare.dev | Blogging Molly";
```

Slap some more `<div>` elements in there:

```
<div style={Styles.navigation.bar}>
    <div style={Styles.navigation.text}>{this.TITLE}</div>
</div>
```

Styling them is also relatively straightforward. Let's make it nearly black, with white monospace text:

```
static navigation = {
    bar: {
        width: "100%",
        height: "59px",
        backgroundColor: "rgb(30, 30, 30)"
    },
    text: {
        color: "rgb(245, 245, 245)",
        lineHeight: "59px",
        marginLeft: "15px",
        fontFamily: "monospace",
        fontSize: "1.6em"
    }
};
```

It looks just right:

![Image](https://aare.dev/posts/images/1-4.nav-bar.png)

### Final Notes

It looks like I jumped the gun, the navigation dependency was added, but I didn't even get to using it.

Either way, that'll do one afternoon.

I'm out.














