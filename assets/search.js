const GEMINI_API_KEY = "AIzaSyDdIWu-5sbzY4WqwLLoDLCTgOSLA4vK4OI";
const DATA_URL = "/Mohammad-Abdulwahhab/mohammad_indexed_content.json";

const VIDEO_MAP = {
    // Basics
    "90ujp5xWsLg": "basics-of-organic-chemistry/",
    "CnxEUKheEMw": "basics-of-organic-chemistry/",
    "GXakjcJraz0": "basics-of-organic-chemistry/",
    "--xUdPx-2eQ": "basics-of-organic-chemistry/",
    "lXI2uvX-SxA": "basics-of-organic-chemistry/",
    "ZqJhr9Z88AI": "basics-of-organic-chemistry/",
    "E16wBtAqBws": "basics-of-organic-chemistry/",
    "bBWugIwsCOE": "basics-of-organic-chemistry/",
    "dVn1RvFVa8g": "basics-of-organic-chemistry/",
    "vY1tmu9XhM4": "basics-of-organic-chemistry/",
    "2mzgjz0xgaA": "basics-of-organic-chemistry/",
    "EmrKtZyMsgE": "basics-of-organic-chemistry/",
    // Organic I
    "2_I8_9yLy7g": "organic-i/",
    "zo2GuxG6y4o": "organic-i/",
    "ZLbGVBCKoaE": "organic-i/",
    "WC66sjrBiwg": "organic-i/",
    "oJKKRrbvH4Y": "organic-i/",
    "buNXJ0cb7b8": "organic-i/",
    "oVeUdXux10M": "organic-i/",
    "S5FPdPxzW-Q": "organic-i/",
    "a2kWyeQA6NE": "organic-i/",
    "G6qBHmVw41g": "organic-i/",
    "Q2J20RAYqPg": "organic-i/",
    "eqp4FBZnWOc": "organic-i/",
    "LbWUyG7NCaI": "organic-i/",
    // Organic II
    "Z9RJ-UsM06E": "organic-ii/",
    "TWIskII3KL8": "organic-ii/",
    "XuyR0tj4Bkk": "organic-ii/",
    "Bxu6xF_XD3E": "organic-ii/",
    "NmwMNsYBxKE": "organic-ii/",
    "glUXuy-KF0A": "organic-ii/",
    "QAUfzhDxKEg": "organic-ii/",
    "527wE0td1eM": "organic-ii/",
    "BjMrn7BN--s": "organic-ii/",
    "s3A8kNHm2tA": "organic-ii/",
    "SVuEVpFWciY": "organic-ii/",
    "gzwVVq6I7qY": "organic-ii/",
    "gY-RxL0pZKo": "organic-ii/",
    "4J9pJJjnOls": "organic-ii/",
    "TigWsawGYvw": "organic-ii/",
    "2obn0dk8GqE": "organic-ii/",
    // Organic III
    "gciMDPQpzEM": "organic-iii/",
    "T_pCI8Gxpbs": "organic-iii/",
    "Sg9ckDOWTBo": "organic-iii/",
    "X6-ESnC-8Pc": "organic-iii/",
    "ADRwmPsDf3Q": "organic-iii/",
    "NEApj9fLuRk": "organic-iii/",
    "C-jjRmDI8uE": "organic-iii/",
    "W8PAy8bcI00": "organic-iii/",
    "uNBXUFLT2Ks": "organic-iii/",
    "6qlVOLBUWVk": "organic-iii/",
    "VQepcr-tuMU": "organic-iii/",
    "cD0LZ5fIBqE": "organic-iii/",
    "bJpZoQ2CLbw": "organic-iii/",
    "PGvIO2cBNbA": "organic-iii/",
    "dAmOMgGEv6w": "organic-iii/"
};

let videoMetadata = [];

async function initSearch() {
    try {
        const response = await fetch(DATA_URL);
        videoMetadata = await response.json();
        console.log("Video metadata loaded:", videoMetadata.length);
    } catch (error) {
        console.error("Error loading video metadata:", error);
    }
}

async function performAISearch(query) {
    const statusEl = document.getElementById('searchStatus');
    const resultsEl = document.getElementById('searchResults');
    const btnEl = document.getElementById('searchBtn');

    const normalizedQuery = query.toLowerCase().trim();
    const cacheKey = `search_cache_${normalizedQuery}`;

    if (!videoMetadata || videoMetadata.length === 0) {
        await initSearch();
        if (!videoMetadata || videoMetadata.length === 0) {
            statusEl.innerText = "Error: Video data could not be loaded.";
            statusEl.classList.add('active');
            return;
        }
    }

    const cachedResponse = sessionStorage.getItem(cacheKey);
    if (cachedResponse) {
        try {
            const results = JSON.parse(cachedResponse);
            renderResults(results);
            statusEl.innerText = "Showing cached results:";
            statusEl.classList.add('active');
            return;
        } catch (e) {
            sessionStorage.removeItem(cacheKey);
        }
    }

    statusEl.innerText = "Searching... (جاري البحث...)";
    statusEl.classList.add('active');
    resultsEl.classList.remove('active');
    btnEl.disabled = true;
    btnEl.innerHTML = '<div class="spinner"></div> Searching...';

    const systemPrompt = `You are a specialized Chemistry Education AI. Your task is to match a student's query to the best organic chemistry videos from the provided metadata.

STUDENT QUERY: "${query}"

INSTRUCTIONS:
1. Language Detection: Detect if the query is in Arabic or English.
2. Semantic Matching: Match the query's chemistry topics to the English metadata (titles, summaries, keywords).
3. Precision: If the query is in English, provide highly accurate results based on exact and semantic matches.
4. Translation (Arabic Queries): If the query is in Arabic, translate it to standard organic chemistry English terms before matching.
5. Output Language: The "reason" for each result must be in the SAME language as the student's query (Arabic for Arabic queries, English for English queries).
6. Output Format: Return ONLY a valid JSON array of objects. No introductory text.

METADATA:
${JSON.stringify(videoMetadata.map(v => ({id: v.video_id, title: v.title, summary: v.summary, keywords: v.keywords})))}

JSON STRUCTURE:
[{"id": "video_id", "title": "video_title", "reason": "Short explanation of relevance"}]`;

    try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: systemPrompt }] }],
                generationConfig: {
                    temperature: 0.2 // Lower temperature for more consistent JSON
                }
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`API Error: ${response.status}`);
        }

        const data = await response.json();
        let aiResponseText = data.candidates[0].content.parts[0].text;
        
        // Clean up any potential markdown formatting
        const cleanedText = aiResponseText.replace(/```json|```/g, "").trim();
        
        // Find the first [ and last ] to extract the JSON array
        const start = cleanedText.indexOf('[');
        const end = cleanedText.lastIndexOf(']');
        
        if (start === -1 || end === -1) {
            throw new Error("No video results found for this specific query.");
        }
        
        const jsonString = cleanedText.substring(start, end + 1);
        const results = JSON.parse(jsonString);

        if (results.length === 0) {
            throw new Error("No relevant videos found. Try different terms.");
        }

        sessionStorage.setItem(cacheKey, JSON.stringify(results));
        renderResults(results);
    } catch (error) {
        console.error("Search error:", error);
        
        const keywordResults = performKeywordFallback(query);
        if (keywordResults.length > 0) {
            renderResults(keywordResults);
            statusEl.innerText = "Showing matches based on keywords:";
        } else {
            statusEl.innerHTML = `<span style="color:red">No results found.</span><br>Try a broader topic or search in English.`;
        }
    } finally {
        btnEl.disabled = false;
        btnEl.innerHTML = 'Search';
    }
}

function performKeywordFallback(query) {
    const q = query.toLowerCase();
    const matches = videoMetadata.filter(v => 
        v.title.toLowerCase().includes(q) || 
        v.summary.toLowerCase().includes(q) || 
        v.keywords.some(k => k.toLowerCase().includes(q))
    );
    
    return matches.slice(0, 5).map(v => ({
        id: v.video_id,
        title: v.title,
        reason: "Matched your search keywords."
    }));
}

function renderResults(results) {
    const resultsEl = document.getElementById('searchResults');
    const statusEl = document.getElementById('searchStatus');
    
    resultsEl.innerHTML = '';
    
    if (!results || results.length === 0) {
        statusEl.innerText = "No relevant videos found for your query.";
        return;
    }

    statusEl.innerText = `Found ${results.length} relevant videos:`;

    results.forEach(res => {
        const sectionPath = VIDEO_MAP[res.id] || "";
        const videoUrl = `${sectionPath}`; // Link to the section page
        
        const card = document.createElement('div');
        card.className = 'search-result-card';
        card.innerHTML = `
            <div class="result-tag">Recommended Video</div>
            <h3 class="result-title">${res.title}</h3>
            <p class="result-reason">${res.reason}</p>
            <div class="result-footer">
                <a href="${videoUrl}" class="button button-primary">Watch Video</a>
            </div>
        `;
        resultsEl.appendChild(card);
    });

    resultsEl.classList.add('active');
}

// Event Listeners
document.getElementById('searchForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const query = document.getElementById('searchInput').value.trim();
    if (query) {
        performAISearch(query);
    }
});

// Initialize
initSearch();
