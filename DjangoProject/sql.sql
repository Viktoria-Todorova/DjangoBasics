INSERT INTO categories_category (name, description, created_at)
VALUES
(
    'Work',
    'Tasks related to job, meetings, and projects.',
    NOW()
),
(
    'Personal',
    'Personal errands and daily activities.',
    NOW()
),
(
    'Health',
    'Health, fitness, and wellbeing related tasks.',
    NOW()
),
(
    'Learning',
    'Study, reading, and skill development tasks.',
    NOW()
);

INSERT INTO notes_note (
    title,
    body,
    created_at,
    is_published,
    updated_at,
    priority,
    category_id
)
VALUES
(
    'Finish Django todo app',
    'Implement models, views, and templates.',
    NOW(),
    TRUE,
    NOW(),
    3,
    1  -- Work
),
(
    'Prepare meeting slides',
    'Create presentation slides for Monday meeting.',
    NOW(),
    FALSE,
    NOW(),
    2,
    1  -- Work
),
(
    'Buy groceries',
    'Milk, eggs, fruits, vegetables, and bread.',
    NOW(),
    FALSE,
    NOW(),
    2,
    2  -- Personal
),
(
    'Go for a run',
    'Run 5km in the park.',
    NOW(),
    TRUE,
    NOW(),
    2,
    3  -- Health
),
(
    'Read Django documentation',
    'Focus on Django ORM and query optimization.',
    NOW(),
    FALSE,
    NOW(),
    1,
    4  -- Learning
),
(
    'Meditation',
    '10 minutes of mindfulness meditation.',
    NOW(),
    TRUE,
    NOW(),
    1,
    3  -- Health
),
(
    'Plan weekend trip',
    'Look for destinations and book accommodation.',
    NOW(),
    FALSE,
    NOW(),
    1,
    2  -- Personal
);
