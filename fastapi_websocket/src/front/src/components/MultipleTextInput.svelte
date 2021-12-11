<script lang="ts">
    import { createEventDispatcher } from "svelte";
    export let text: string;
    export let fill = false;
    export let width = 120;
    export let editable: boolean;

    let currentText: string;

    const dispatch = createEventDispatcher();
    const style = fill ? "width: calc(100% - 16px);" : `width: ${width}px`;

    function handleInput(e: Event) {
        currentText = (e.target as HTMLInputElement).innerHTML;
        currentText = currentText
            .replace(/<div>/gi, "\n")
            .replace(/<br><\/div>$/gi, "\n");
        currentText = currentText
            .replace(/<br><\/div>/gi, "")
            .replace(/(<br>|<\/div>)/gi, "");
        currentText = currentText.replace(/&gt;/gi, ">").replace(/&lt;/gi, "<");
    }

    function handleKeyPress(e: KeyboardEvent) {
        dispatch("keypress", {
            event: e,
            text: currentText,
        });
    }

    function handleClick() {
        dispatch("click", {
            text: currentText,
        });
    }
</script>

{#if editable}
    <div
        class="auto-resize-editable-text"
        {style}
        contenteditable="true"
        on:input={handleInput}
        on:keydown={handleKeyPress}
        bind:textContent={text}
    />
{:else}
    <div
        class="auto-resize-editable-text"
        {style}
        contenteditable="false"
        on:click={handleClick}
        bind:textContent={text}
    />
{/if}

<style>
    .auto-resize-editable-text {
        padding: 8px 8px;
        font-size: 14px;
        text-align: left;
        display: inline-block;
        white-space: pre-wrap;
        overflow-wrap: break-word;
        border: solid 1px;
        min-height: 24px;
    }
</style>
