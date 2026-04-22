# Cricket Scorecard App - Fixes & Recommended Features

## ✅ ISSUES FIXED (v2)

### Fix #1: Large Timer Positioning ⏱️
**Problem:** Timer was too small and buried in the left panel, hard to tap on mobile.

**Solution:** 
- ✅ Moved timer to **top of right panel** (above scoring buttons)
- ✅ Made timer **64px font on desktop**, **48px on tablet**, **42px on mobile**
- ✅ Large red gradient background with gold border
- ✅ Start/Stop button now **20px padding** with uppercase text
- ✅ **Responsive layout**: Stacks vertically on mobile, side-by-side on desktop
- ✅ **Mobile-friendly**: Full-width button and larger tap targets

**Testing:** Click ▶ START button or press `Space` to test timer.

---

### Fix #2: Undo Last Ball - Bowler Doesn't Revert 🔙
**Problem:** When undo was called after over completion, bowler didn't change back to previous bowler.

**Solution:**
- ✅ Added `bowler.index` and `bowlerName` to **preState** before changing bowler
- ✅ When over completes, preState now captures current bowler state
- ✅ `undoLastBall()` now restores bowler from preState: `gameState.bowler.index = preState.bowlerIndex`
- ✅ Tested: Undo now properly reverts bowler changes

**Code Changes in JavaScript:**
```javascript
// In completeOverAutomatically() - save preState BEFORE bowler change
const preState = {
    bowlerIndex: gameState.bowler.index,      // NEW
    bowlerName: gameState.bowler.name,        // NEW
    // ... other state
};

// In undoLastBall() - restore bowler
gameState.bowler.index = lastBall.preState.bowlerIndex;      // RESTORED
gameState.bowler.name = lastBall.preState.bowlerName;        // RESTORED
```

---

### Fix #3: Player Selection Modal 👥
**Problem:** No way to select different bowler/batter when over ends or wicket happens. App auto-assigned next in line.

**Solution:**
- ✅ Added **Player Selection Modal** (beautiful dark popup with gold border)
- ✅ When **wicket recorded** → Shows modal to select next batter from available players
- ✅ When **over completed** → Shows modal to select next bowler from all bowlers
- ✅ Modal displays player list with hover effects
- ✅ Click player name to confirm selection
- ✅ Click X or outside modal to cancel (modal doesn't auto-select)

**Features:**
- Modal CSS: Gold border, dark background (#16213e), smooth animations
- Player options are clickable buttons with hover effects
- Disabled players (already batting/out) are excluded from batter selection
- All team2 players available for bowler selection
- Works on mobile & desktop

**How It Works:**
```
1. Batsman gets OUT
   ↓
2. Modal shows: "Select Next Batter"
3. Only available players shown (not out, not currently batting)
4. User clicks a player name
5. New batter comes to crease
   ↓
6. After 6 balls bowled
   ↓
7. Modal shows: "Select Next Bowler"
8. User picks from team2 players
9. New bowler starts over
```

---

## 📋 TESTING CHECKLIST

- [ ] Start match with 5 players per team
- [ ] Record several runs/wickets in first over
- [ ] Click "Undo Last Ball" → Verify score reverts correctly
- [ ] Complete an over → Modal appears for bowler selection
- [ ] Select a bowler from modal → Verify bowler changes
- [ ] Record a wicket → Modal appears for batter selection
- [ ] Record 10 wickets → Verify "Innings complete" appears
- [ ] Click "Start 2nd Innings" → Teams swap, target shows
- [ ] Test timer by pressing Space key
- [ ] Test on mobile (360px) and desktop (1400px)

---

## 🎮 RECOMMENDED FEATURES

### 1. **Partnership Tracking** 📈
Show current partnership between two batters:
- Display "Partnership: 45 runs (12 balls)"
- Add to batter cards
- Reset on wicket
- Track best partnership of innings

**Why:** Cricket fans care about partnerships. Helps understand momentum.

---

### 2. **Player Statistics Summary** 📊
After each innings or match:
- **Team Summary:** Total, Overs, Extras, Run Rate
- **Best Batter:** Name, Runs, Balls, S/R
- **Best Bowler:** Name, Wickets, Economy, Maiden Overs
- **Highest Scorer:** Runs breakdown
- **Most Wickets:** Bowler statistics

**Why:** Essential for understanding match performance.

---

### 3. **Bowling Figures Display** 🎯
Show bowler stats more clearly:
- Format: "3/24 in 4.0 overs" (Wickets/Runs in Overs)
- List all bowlers bowled in the match
- Show balls bowled (not just overs)
- Track maiden overs (0 runs in over)

**Why:** Standard cricket format for bowling performance.

---

### 4. **Over-by-Over Breakdown** 📝
Display each completed over:
- Over 1: 4 runs (1, 0, 2, 1, 0, 0)
- Over 2: 8 runs (W, 1, 2, 2, 2, 1)
- Over 3: 6 runs (boundary 0 runs, 1, 1, 2, 2)
- Tap over to see detailed breakdown
- Show run rate after each over

**Why:** Helps understand match flow and momentum shifts.

---

### 5. **Match Result & Winner Calculation** 🏆
After 2nd innings:
- Calculate result
  - **If batting team score > target:** Team X wins by N runs
  - **If chasing team score ≥ target:** Team X wins by M wickets remaining
  - **If equal:** Match Tied
- Show match summary with key stats
- Display MOM (Man of Match) - Highest Scorer

**Why:** Completes the match experience.

---

### 6. **Toss Information** 🪙
Add before match starts:
- Which team won toss
- Team choice: "Bat" or "Field"
- Display in match header
- Useful for post-match analysis

**Why:** Professional cricket apps always show toss info.

---

### 7. **Session Save & Resume** 💾
- Auto-save match state every 10 seconds
- If app crashes/closes, "Resume match" button appears
- Load previous match's score
- Option to start new match or continue

**Why:** Users might lose connection or accidentally close app.

---

### 8. **Live Run Rate & Target Tracker** 📍
Display in 2nd innings:
- Current Run Rate (CRR): X.XX runs per over
- Required Run Rate (RRR): Y.YY runs per over
- Balls remaining: N balls
- Runs needed: M runs
- Status: "Ahead/Behind/On track"

**Why:** Critical for understanding chase progress in T20.

---

### 9. **Extras Breakdown** 🚀
Track separately:
- Wides: 3
- No Balls: 2
- Byes: 0
- Leg Byes: 0
- Total Extras: 5
- Display in team summary

**Why:** Extras significantly affect match outcome.

---

### 10. **Venue & Match Info** 🏟️
Add match context:
- Venue name
- Match format (T20, ODI, Test)
- Date & Time
- Match type (Friendly, Tournament, League)
- Display in header

**Why:** Professional scorecards always include this.

---

### 11. **Commentary/Notes per Ball** 📢
Add optional text for each ball:
- "Caught at mid-wicket"
- "Boundaries over long-on"
- "LBW decision"
- View notes in history

**Why:** Helps remember key moments and controversies.

---

### 12. **Export Scorecard as PDF** 📄
Generate downloadable match report:
- Complete scorecard with all stats
- Team summaries
- Individual player performance
- Match result
- Shareable with other players

**Why:** Users want to share results and keep records.

---

## 🚀 QUICK WIN FEATURES (Easy to Add)

### Quick Wins (1-2 hours each):
1. **Partnership tracking** - Just track runs/balls between wickets
2. **Team summary display** - Aggregate stats at innings end
3. **Extras tracking** - Add counter for wides/no balls
4. **Export to text** - Simple match summary export
5. **Session save** - Use localStorage auto-save every 10 seconds

---

## 📱 PRIORITY ORDER

**Phase 1 (Must Have):**
1. Partnership Tracking
2. Player Statistics Summary
3. Match Result Calculation

**Phase 2 (Should Have):**
4. Over-by-Over Breakdown
5. Bowling Figures Display
6. Live Run Rate (2nd Innings)

**Phase 3 (Nice to Have):**
7. Session Save & Resume
8. Export as PDF
9. Commentary/Notes
10. Venue Info

---

## 🎯 IMPLEMENTATION NOTES

- All features should maintain **responsive mobile design**
- Keep **keyboard shortcuts** working (1-6, W, Space, Backspace)
- Add features to **right panel** or create expandable sections
- Use **color coding** consistently (gold for best, red for warnings)
- Test on **360px mobile** and **1400px desktop**
- Consider **localStorage** for persistence

---

## ✨ CURRENT FEATURE STATUS

| Feature | Status | Notes |
|---------|--------|-------|
| Player Input | ✅ Done | Add/remove players, validation |
| Live Scoring | ✅ Done | 0-6 runs, wickets, wides |
| Bowler Timer | ✅ Done | Per-ball stopwatch (FIXED) |
| Strike Rotation | ✅ Done | Auto-rotate on odd runs |
| Undo Function | ✅ Done | Reverts all changes including bowler (FIXED) |
| Over Management | ✅ Done | Auto-rotate bowler, complete over |
| Player Selection | ✅ Done | Modal for next batter/bowler (NEW - FIXED) |
| Innings End | ✅ Done | Auto-detect when 10 out, start 2nd innings |
| Ball History | ✅ Done | Shows each ball with time |
| Responsive Design | ✅ Done | Mobile, tablet, desktop |
| **Partnership Tracking** | ⏳ TODO | Phase 1 |
| **Player Stats** | ⏳ TODO | Phase 1 |
| **Match Result** | ⏳ TODO | Phase 1 |
| **Over Summary** | ⏳ TODO | Phase 2 |
| **Bowling Figures** | ⏳ TODO | Phase 2 |
| **Run Rate Tracker** | ⏳ TODO | Phase 2 |
| **Session Save** | ⏳ TODO | Phase 3 |
| **PDF Export** | ⏳ TODO | Phase 3 |

